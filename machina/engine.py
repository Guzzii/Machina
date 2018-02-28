from machina.src.core import compute_cost
from seaborn import set

import matplotlib.pylab as plt


class Client(object):
    def __init__(self, plans, n_member=1, self_contri=0, tax_fac=0.):
        self._n_mem = n_member
        self._tax = 1 - tax_fac

        plans['cost_per_year'] = 26*plans['cost_per_paycheck']
        plans.loc[plans.name == 'HSA', 'self_contribution'] = self_contri
        plans['tax_rate'] = self._tax

        self._plans = plans
        self._n_plans = plans.name.nunique()

    @property
    def n_member(self):
        return self._n_mem

    @n_member.setter
    def n_member(self, val):
        self._n_mem = val

    def __repr__(self):
        repr = 'A family of %d considers purchasing one of the %s plans'
        return repr % (self._n_mem, self._n_plans)

    def _match_plans(self):
        self._sub_plans =\
            self._plans[self._plans.members == self._n_mem].copy()

    def fit(self, iter=300):
        self._match_plans()

        cols = ['name', 'members', 'cost_per_year', 'deductible',
                'co_insurance', 'out_of_pocket', 'company_contribution',
                'self_contribution', 'tax_rate']
        self._sub_plans = self._sub_plans[cols]

        set()
        x = list(range(100, iter*100+1, 100))

        cost_dict = {}
        for row in self._sub_plans.itertuples():
            tup = map(float, row[3:])
            cost_dict[row[1]] = compute_cost(*tup, iter)
            plt.plot(x, cost_dict[row[1]], label=row[1])

        plt.ylabel('Total cost (after-plan, after-tax)')
        plt.xlabel('Raw Medical Cost')
        plt.legend()
        plt.show()
        plt.close()

        self._cost_dict = cost_dict

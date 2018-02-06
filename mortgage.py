# Introduction to Computation and Programming using Python
"""Calculate the interest paid on three different types of mortgages"""


def find_payment(loan, monthly_rate, months):
    """Assumes: loan and r are floats, m an int
       Returns the monthly payment for a mortgage of size
       loan at a monthly rate of r for m months"""
    return loan * ((monthly_rate * (1 + monthly_rate)**months)
                   / ((1 + monthly_rate)**months - 1))


class Mortgage(object):
    """Abstract class for building different kinds of mortgages"""

    def __init__(self, loan, ann_rate, months):
        """Create a new mortgage"""
        self.loan = loan
        self.rate = ann_rate / 12.0
        self.months = months
        self.paid = [0.0]
        self.owed = [loan]
        self.payment = find_payment(loan, self.rate, months)
        self.legend = None  # description on mortgage

    def make_payment(self):
        """Make a payment"""
        self.paid.append(self.payment)
        reduction = self.payment - self.owed[-1] * self.rate
        self.owed.append(self.owed[-1] - reduction)

    def get_total_paid(self):
        """Return the total amount paid so far"""
        return sum(self.paid)

    def __str__(self):
        return self.legend


class Fixed(Mortgage):
    """Returns the fixed mortgage interest"""

    def __init__(self, loan, monthly_rate, months):
        Mortgage.__init__(self, loan, monthly_rate, months)
        self.legend = 'Fixed, ' + str(monthly_rate*100) + '%'


class FixedWithPts(Mortgage):
    """Returns interest paid of fixed rate with points"""

    def __init__(self, loan, monthly_rate, months, pts):
        Mortgage.__init__(self, loan, monthly_rate, months)
        self.pts = pts
        self.paid = [loan * (pts/100.0)]
        self.legend = 'Fixed, ' + str(monthly_rate*100) + '%, '\
                      + str(pts) + ' points'


class TwoRate(Mortgage):
    """Returns interest paid on two rate mortgage"""

    def __init__(self, loan, monthly_rate, months, teaser_rate, teaser_months):
        Mortgage.__init__(self, loan, teaser_rate, months)
        self.teaser_months = teaser_months
        self.teaser_rate = teaser_rate
        self.next_rate = monthly_rate / 12.0
        self.legend = (str(teaser_rate*100)
                       + '% for ' + str(self.teaser_months)
                       + ' months, then ' + str(monthly_rate * 100) + '%')

    def make_payment(self):
        if len(self.paid) == self.teaser_months + 1:
            self.rate = self.next_rate
            self.payment = find_payment(self.owed[-1], self.rate,
                                        self.months - self.teaser_months)
        Mortgage.make_payment(self)


def compare_mortgages(amt, years, fixed_rate, pts, pts_rate,
                      var_rate_1, var_rate_2, var_months):
    """Function takes all data and compares mortgages"""

    tot_months = years * 12
    fixed_1 = Fixed(amt, fixed_rate, tot_months)
    fixed_2 = FixedWithPts(amt, pts_rate, tot_months, pts)
    two_rate = TwoRate(amt, var_rate_2, tot_months, var_rate_1, var_months)
    morts = [fixed_1, fixed_2, two_rate]
    for iii in range(tot_months):
        for mort in morts:
            mort.make_payment()
    for iii in morts:
        print(iii)
        print(' Total payments = $' + str(int(iii.get_total_paid())))

compare_mortgages(amt=200000, years=30, fixed_rate=0.07,
                  pts=3.25, pts_rate=0.05, var_rate_1=0.045,
                  var_rate_2=0.095, var_months=48)

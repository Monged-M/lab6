FEE_PER_HOUR = 1200


class RegularPolicy:
    def fee(self, hours):
        return hours * FEE_PER_HOUR


class ScholarshipPolicy:
    def fee(self, hours):
        return hours * FEE_PER_HOUR * 0.5


class InternationalPolicy:
    RATE = 2000
    SERVICE_FEE = 5000

    def fee(self, hours):
        return hours * self.RATE + self.SERVICE_FEE



def make_invoice(student, kind):
    if kind == "regular":
        policy = RegularPolicy()
    elif kind == "scholarship":
        policy = ScholarshipPolicy()
    elif kind == "international":
        policy = InternationalPolicy()
    else:
        raise KeyError(kind)
    total = policy.fee(student.total_hours)
    text = f"Invoice for {student.student_id}: {int(total)} EGP"
    with open(f"invoice_{student.student_id}.txt", "w") as f:
        f.write(text)
    return total

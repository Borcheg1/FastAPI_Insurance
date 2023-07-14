from tortoise import Model, fields


class RateModel(Model):
    id = fields.UUIDField(pk=True)
    cargo_type = fields.CharField(max_length=150, null=False)
    current_rate = fields.DecimalField(max_digits=8, decimal_places=6, null=False)
    date_from = fields.DateField(default=None, null=False)

    class Meta:
        table = "ratemodel"

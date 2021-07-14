from pymodm import MongoModel, fields

class User(MongoModel):
    client_id = fields.CharField(primary_key=True)
    access_token = fields.CharField()
    refresh_token = fields.CharField()
    expires_in = fields.FloatField()

class Deal(MongoModel):
    deal_id = fields.IntegerField(primary_key=True)
    name = fields.CharField()
    stage = fields.CharField()
    close_date = fields.DateTimeField(blank=True)
    amount = fields.FloatField(blank=True)
    deal_type = fields.CharField(blank=True)

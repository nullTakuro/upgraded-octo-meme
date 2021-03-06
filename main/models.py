from django.db import models

# Create your models here.
# After each edit run this = python manage.py makemigrations login
# and then this = python manage.py migrate

# As with ForeignKey, you can also create recursive relationships (an object with a many-to-many relationship to itself) and relationships to models not yet defined.


class user(models.Model):
    # userID is auto Generated
    username = models.CharField(editable=False, max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, default='UNDEFINED')      # As the value for this data is to be assigned below as the default return value for when a search query is run pertaining to this data its value cannot be null so a defualt value must be assigned!
                                                                 # A CharField that checks that the value is a valid email address. It uses EmailValidator to validate the input.
    profile_pic = models.URLField(max_length=1000)       # A CharField for a URL.

    def __str__(self):
        return self.username        # Returns the specific value as the value of the username

class property(models.Model):
    # propertyID is auto Generated
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)        #uses the primary key asssigned to each user and imports it as a ForeignKey into the Property table. When a user is deleted the Propert associated is also deleted!
    assigned_name = models.CharField(max_length=30, default='UNDEFINED')      # As the value for this data is to be assigned below as the default return value for when a search query is run pertaining to this data its value cannot be null so a defualt value must be assigned!

    def __str__(self):
        return self.assigned_name        # Returns the specific value as the value of the assigned_name

class user_address(models.Model):
    # addressID is auto Generated
    property_id = models.ForeignKey(property, on_delete=models.CASCADE)        # A many-to-one relationship. Requires a positional argument: the class to which the model is related.
    line_one = models.CharField(max_length=50)
    line_two = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

class booking(models.Model):
    # bookingID is auto Generated
    property_id = models.ForeignKey(property, on_delete=models.CASCADE)      # A many-to-one relationship. Requires a positional argument: the class to which the model is related.
    start_datetime = models.DateTimeField(auto_now=False, auto_now_add=False)        # A date and time, represented in Python by a datetime.datetime instance
    duration = models.DurationField()       # A field for storing periods of time - modeled in Python by timedelta. When used on PostgreSQL, the data type used is an interval and on Oracle the data type is INTERVAL DAY(9) TO SECOND(6).
    end_datetime = models.DateTimeField(auto_now=False, auto_now_add=False)        # A date and time, represented in Python by a datetime.datetime instance

class guest(models.Model):
    # guestID is auto Generated
    booking_id = models.ForeignKey(booking, on_delete=models.CASCADE)       # A many-to-one relationship. Requires a positional argument: the class to which the model is related.
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=14)
    email = models.EmailField(max_length=254)       # A CharField that checks that the value is a valid email address. It uses EmailValidator to validate the input.


class guest_address(models.Model):
    # addressID is auto Generated
    guest_id = models.ForeignKey(guest, on_delete=models.CASCADE)        # A many-to-one relationship. Requires a positional argument: the class to which the model is related.
    line_one = models.CharField(max_length=50)
    line_two = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

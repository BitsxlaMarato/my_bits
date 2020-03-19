from django.db import models
from user.models import User

BAG_ADDED = 'A'
BAG_REMOVED = 'R'

BAG_STATUS = (
    (BAG_ADDED, 'Added'),
    (BAG_REMOVED, 'Removed')
)

BAG_BUILDINGS = (
    ('E01', 'E01'),
    ('E02', 'E02')
)


class Room(models.Model):
    """Represents a room where a position can be"""

    # Room identifier
    room = models.CharField(primary_key=True, max_length=63, null=False, choices=BAG_BUILDINGS)
    # Number of rows
    row = models.PositiveIntegerField(null=False, default=0)
    # Number of columns
    col = models.PositiveIntegerField(null=False, default=0)
    # Nearest row to the door
    door_row = models.PositiveIntegerField(null=False, default=0)
    # Nearest col to the door
    door_col = models.PositiveIntegerField(null=False, default=0)

    def __str__(self):
        return str(self.room)


class Bag(models.Model):
    """Represents a baggage item"""

    STATUS = (
        (BAG_ADDED, 'Added'),
        (BAG_REMOVED, 'Removed')
    )

    # Item identifier
    bid = models.AutoField(primary_key=True)
    # User owner of the item
    owner = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name='%(class)s_baggage_owner')
    # User that checked-in the baggage
    inby = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name='%(class)s_baggage_in')
    # User that checked-out the baggage
    outby = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='%(class)s_requests_out')
    # Reflects the status of the item
    status = models.CharField(max_length=1, null=False, default=BAG_ADDED, choices=BAG_STATUS)
    # Reflects the room where the item is/was
    room = models.ForeignKey(Room, null=True, on_delete=models.PROTECT)
    # Reflects the row where the item is/was
    row = models.CharField(max_length=15, null=False)
    # Reflects the column where the item is/was
    col = models.PositiveIntegerField(null=False)
    # Type of item
    btype = models.CharField(max_length=255, null=False)
    # Primary color of the item
    color = models.CharField(max_length=255, null=False)
    # Description of the item
    description = models.TextField(max_length=1023, null=True, blank=True)
    # Reflects if the item is special (different behaviour then) or not
    special = models.BooleanField(default=False)
    # Time for when the item was created
    time = models.DateTimeField(auto_now=False, auto_now_add=True)
    # Time for when the time was updted
    updated = models.DateTimeField(auto_now=True)
    # Image of the bag object
    image = models.FileField(upload_to='baggage', null=True, blank=True)

    def __str__(self):
        return str(self.bid)

    def position(self):
        if self.special:
            return '@' + str(self.col)
        return str(self.row) + str(self.col)




def increment_room_count(sender,instance,created,**kwarg):
    if created:
        if instance.stream_room:
            instance.stream_room.room_count +=1
            instance.stream_room.save()




def decrement_room_count(sender, instance, **kwargs):
    room = instance.stream_room
    room.room_count -= 1
    room.save()

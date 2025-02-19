from django.utils.timezone import now
from .models import UserProfile

def check_and_deduct_credits(user):
    profile, created = UserProfile.objects.get_or_create(user=user)
    
    # Reset credits if it's a new day
    if profile.last_updated != now().date():
        profile.credits = 5
        profile.last_updated = now().date()
    
    # Deduct 1 credit
    if profile.credits > 0:
        profile.credits -= 1
        profile.save()
        return True
    return False

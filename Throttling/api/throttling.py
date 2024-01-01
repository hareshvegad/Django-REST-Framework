from rest_framework.throttling import UserRateThrottle 

class JackRateThottle(UserRateThrottle):
    scope = 'jack'
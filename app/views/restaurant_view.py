def render_restaurant_list(restaurants):
    return [
        {
            "user_id": user.id,
            "restaurant_id": restaurant.id,
            "reservation_date": reservation.date,
            "num_guest": num.guest,
            "special_requests":special.request,
            "status":status,
        }
        for restaurant in restaurants
    ]


def render_restaurant_detail(restaurant):
    return {
        "user_id" : user.id,
        "restaurant_id" : restaurant.id,
        "reservation_date" : reservation.date,
        "num_guest" : num.guest,
        "special_requests" : special.requests,
        "status" : status,
    }

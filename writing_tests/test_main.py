from main import get_weather

def test_get_weather():
    temp_vals = [3, 14, 20, -12, 0.2, 44, 10.0, 10.1, 10.01, 9.99]
    for temp_val in temp_vals:
        assert get_weather(temp_val) == "Hot"

#assert --> will tell us wheter a condition is true or false
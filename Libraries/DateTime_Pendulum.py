# https://pendulum.eustace.io/

import pendulum

now = pendulum.now("Europe/Amsterdam")

print(now.in_timezone("America/Toronto"))
print(now.to_iso8601_string())
print(now.add(hours=-1))
print(now.format('dddd DD MMMM YYYY'))
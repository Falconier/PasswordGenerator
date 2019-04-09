##region File Info:
# File Name: guidExample.py
# globaly unique identifier or GUID's for short
# https://docs.python.org/2/library/uuid.html
##endregion

import uuid

guid = uuid.uuid4()  ##produces a standard GUID

strGUID = str(guid)  ##or str(uuid.uuid4())

hexGUID = uuid.uuid4().hex  ##basically just removes the '-'s from the standard

byteGUID = uuid.uuid4().bytes  ##no idea why on earth you would ever need this, but this splits the guid into its raw bytes

print(guid)
print(strGUID)
print(hexGUID)
print(byteGUID)

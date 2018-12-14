from inky import InkyPHAT
inky_display = InkyPHAT("yellow")
inky_display.set_border(inky_display.BLACK)

from PIL import Image, ImageFont, ImageDraw
img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

from font_fredoka_one import FredokaOne
font = ImageFont.truetype(FredokaOne, 20)

import fcntl, socket, struct
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])
def getHwAddr(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
    return ':'.join(['%02x' % ord(char) for char in info[18:24]])


draw.rectangle((0, 0, inky_display.WIDTH, inky_display.HEIGHT), fill=inky_display.BLACK)

message0 = "******wlan0 info*****"
w, h = font.getsize(message0)
draw.text((0, 0), message0, inky_display.YELLOW, font)

titleIp = "ip:"
ipAddress = get_ip_address('wlan0')
w, h = font.getsize(ipAddress)
draw.text((0, 22), titleIp, inky_display.YELLOW, font)
draw.text((50, 22), ipAddress, inky_display.WHITE, font)

titleMac = "mac:"
macAddress = getHwAddr('wlan0')
w, h = font.getsize(macAddress)
draw.text((0, 44), titleMac, inky_display.YELLOW, font)
draw.text((50, 44), macAddress, inky_display.WHITE, font)

titlePorts = "port:"
w, h = font.getsize(titlePorts)
draw.text((0, 66), titlePorts, inky_display.YELLOW, font)
message80 = "80,"
w, h = font.getsize(message80)
draw.text((50, 68), message80, inky_display.WHITE, font)
message443 = "443"
w, h = font.getsize(message443)
draw.text((80, 68), message443, inky_display.YELLOW, font)

inky_display.set_image(img)
inky_display.show()
from xml.etree.ElementTree import TreeBuilder


while True:
    code = input()
    if code == "END":
        break
    print(code[::-1])
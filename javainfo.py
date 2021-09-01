from java.lang import System

print("Your JRE version is", System.getProperty('java.version'))
print("You're using Java from vendor", System.getProperty('java.vendor'))
print("The current class path is", System.getProperty('java.class.path'))
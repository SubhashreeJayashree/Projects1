import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

# Press CTRL-C to break this loopb
while True:
    import sys

    kernel.respond("some input")
    sys.path.append('/path/to/aiml/directory')
    print(kernel)
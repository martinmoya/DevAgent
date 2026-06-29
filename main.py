from core.kernel import Kernel

def main():

    kernel = Kernel()

    try:
        kernel.initialize()
        kernel.run()

    finally:
        kernel.shutdown()

if __name__ == "__main__":
    main()
    
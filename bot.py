import asyncio
from playwright.async_api import async_playwright, TimeoutError

# Yahan apna answer set karein ("A", "B", "C", ya "D")
ANSWER = "B"

# Yahan apne accounts ki list daal dein
accounts = [
    
  {"username": "Random-1", "wallet": "Ae764YENoTrXw9ZhNE5gCSh7UZp7n9c5Vna5bx9ab9Nh"},
  {"username": "Random-2", "wallet": "AvnGsvqhfNTTgj3DnYC6KqR1gbW8cmu5aRMRKnAiHEgX"},
  {"username": "Random-3", "wallet": "EwqEXomQURb9vExVywJYv9Lt7R6hAoVMvyUhiyFGUxNy"},
  {"username": "Random-4", "wallet": "9irVKyuKtLFMBpFmvm4SYTUVvwgohafaUvkBVtdbmJNZ"},
  {"username": "Random-5", "wallet": "BJwXfcGNPNYkuT9LAXe79GEnRXhoFiPfE6hdCHjoX6V"},
  {"username": "Random-6", "wallet": "6NkyNNHqDX7TZwYLHC3LpYnheoH2KLnRV2nUFeYH5VtC"},
  {"username": "Random-7", "wallet": "7ABbWXPYhaNXzCLxDfZMfg18bduyYbzPH7ysfxWLarea"},
  {"username": "Random-8", "wallet": "349M4AnPd113RhzkWRJ4mgbc12CJsLJVa7jHrFUieC8o"},
  {"username": "Random-9", "wallet": "976kebVQFnUUFgHuWYpimCL2AdVSysPNEXQNrQvpZ6tY"},
  {"username": "Random-10", "wallet": "CY4mMeN9dka1QumJqhmnFTYB24T6A8VbFrdkeNcapJZC"},
  {"username": "Random-11", "wallet": "DaZFSp5T6sf731NPueGkHj7pb6bpmKXs7So4uRpfDqb7"},
  {"username": "Random-12", "wallet": "4A7Lfju7npV3xq9YT82nUAneBQtpp13pAQZzwbD45ZD5"},
  {"username": "Random-13", "wallet": "9QQaP8PA2gMBZMT8UeFwZXsAQW2fg5vkimHWadsb7nDG"},
  {"username": "Random-14", "wallet": "HSsuKw8VpnV7kE6wjwrJgjQCkKvd1XDYUYFuuiCprqpa"},
  {"username": "Random-15", "wallet": "xeDAuvzLM6KriyzxZCj8ejfKEEknSFdr3EwCUenzATE"},
  {"username": "Random-16", "wallet": "2hjBS7WBmEcnAS2tSmkCcGJQaVayJJpxuUp4ckmhHwkR"},
  {"username": "Random-17", "wallet": "7LRhonRNeYkuYsDNRrRQQjZmAhcpudkWSBK3634WBsz2"},
  {"username": "Random-18", "wallet": "8c6E4rAd5b3D9gWQ1m6FnZMeFbaNUJmcnkyxREDM5CVq"},
  {"username": "Random-19", "wallet": "G62B5e4sZWXUTkCDWZfKfMQ3AVWbcMo4zeqdVvMznsEh"},
  {"username": "Random-20", "wallet": "L178Th1K6KXJ1jNJh6t3ypJnMhTeRjjBwMsmQsFjGae"},
  {"username": "Random-21", "wallet": "8RLL5ZpPe7pdjcFS7fLX9awzGy8q3firukkaCDxUk5pZ"},
  {"username": "Random-22", "wallet": "4DMpWrWTj2U4hooWuQPUBH29q92Fbt9QYb2iGpfzVDDm"},
  {"username": "Random-23", "wallet": "FGLW7ReCu2e5suAVHweAgPKFRML8sEnvvBFhWPZC3tud"},
  {"username": "Random-24", "wallet": "CuZ1FURepQ449rUL2MXUCnDaxXE6ZRcj8HzcZdwXqhM6"},
  {"username": "Random-25", "wallet": "4J9ofjsiJW8kMJAN6BCcHuQPzoNiyX1GCRmXnreBYCL8"},
  {"username": "Random-26", "wallet": "5VWi6ZeEueKjyjf4NWbenCUxQJQ1xN2Q5i44eHQ6n286"},
  {"username": "Random-27", "wallet": "CMNtgLSTHzMexxgd62ufn7WT6uDKDhksHTzvTApjmqA4"},
  {"username": "Random-28", "wallet": "2diRndvtjGn6fMikcDo6eHkvzCGZCyX9HgokowewtTcs"},
  {"username": "Random-29", "wallet": "3q7isMQ2ug4vK5bwzUjb39Eb5KoZ3SE7wt2aqvjtUpwZ"},
  {"username": "Random-30", "wallet": "9tHwrFaSM9xXiXq6ygwEgRGQ4WBSZ3qZdfwN1xBqmpU7"},
  {"username": "Random-31", "wallet": "3zhdoMdmnJdFPz1kNJtZHU93h4r12SJwuGxSQ2biFqct"},
  {"username": "Random-32", "wallet": "HWQeVqkQ7V6LSbwTY4K5qS1ThSSUTaVzfHUzZUvBrprs"},
  {"username": "Random-33", "wallet": "2Fw8ZaYjLWgNKa144W8B62Se8xnxf2cNvcMxkXg5x5vZ"},
  {"username": "Random-34", "wallet": "2iQHfYQi4j2THeLg2Tmj5bET73rj8ZiuRnANHZsDGECK"},
  {"username": "Random-35", "wallet": "Fd1JkZkUZQBfEDnyWnr3VW9XU8EmsS28wiYC6wZPfF2G"},
  {"username": "Random-36", "wallet": "Haq7b5Ho5JJJj6S2sX7wCB2jEgpmivmqbge5PMB6Ztfb"},
  {"username": "Random-37", "wallet": "7a1sj81Tv84FL1kabLdpBrnqvMBc5ydNBi7ZuacvQxzY"},
  {"username": "Random-38", "wallet": "9sR44TPihTNB2CESJs42GR2n4812HuTThJNFZfnwUvMZ"},
  {"username": "Random-39", "wallet": "CgR11kQTC2RJsdS5L3FZTqat46ueb1iji1g7ATCdFCYr"},
  {"username": "Random-40", "wallet": "ECKwFWVtNpNRyH3PUpWnR4WTxd4HyZCx5JNzdvTW3U3B"},
  {"username": "Random-41", "wallet": "J9E819prScPEGrpWTKd433c5hUANbt7rsU5W4smcMuXy"},
  {"username": "Random-42", "wallet": "HHA94SjuZZr4ScedA81oESXzhgMgyAhooW82jkk628uu"},
  {"username": "Random-43", "wallet": "GKtzPAa2eR1SwECCNp1ycQm4i2g7Dz6sLXSoBWtaf8L7"},
  {"username": "Random-44", "wallet": "A2idZzPJmG3DRwNJKqSD8TwkWwboCGkwtrQKPbzZ9Zs6"},
    {"username": "Random-45", "wallet": "CQspVzEsdHHS58ZK1QGSLPPvbCp3CeTVCVHgt83LfpAc"},
  {"username": "Random-46", "wallet": "FeaeQkRwAXz5ksM2KsegpEgoH1sjqgk3iknPbUC73dDX"},
  {"username": "Random-47", "wallet": "24TCtPBJmRKNbCvUt7XhAY6S2qiyGC3oF3MTebf23LAx"},
  {"username": "Random-48", "wallet": "3uNNwjFLLhgo1VmnkvvavVGfvw1wV6uo4rW3JkgmLgss"},
  {"username": "Random-49", "wallet": "46GzgmeVxd9MnNNwGxKABDV38573egTmrkUJpYQyhgBt"},
  {"username": "Random-50", "wallet": "Bk4hgGe6KTgHJXN2Q8779TYoeEEV4DJHpyxyVWg7v3X9"},
   
  {"username": "Random-51", "wallet": "6ibqktihM5ohEyFPmnvWtYEkPajgqjujcuFVPEdRpoNM"},
  {"username": "Random-52", "wallet": "9ukGwKV4pyoptaKwW1LuDCZkTEQgNdUbspkarn5Z4LjK"},
  {"username": "Random-53", "wallet": "8nEx1AT7QVTfKudS2937jHpndBmX9mF3yKjZc1vyxofz"},
  {"username": "Random-54", "wallet": "J3niTpMvQEwMdeKhpUr5vykdcNNxt9q4mKbnQXdiArL2"},
  {"username": "Random-55", "wallet": "4BRrrqmAa2UmA5vBmq8AqS55mikf3sxzrKxbc2pXifu8"},
  {"username": "Random-56", "wallet": "JBUPWHNGMen4BjQYy3WHFE7aFXhGnHyocKKi1Ha5gBpb"},
  {"username": "Random-57", "wallet": "4ochLaH7KFdeU7oxTAYCii5m3aKgKJyTMDBNX7NXXtpk"},
  {"username": "Random-58", "wallet": "4EeYcX4mHN6UDCjWgqEy8upbkFMVDNG5pgSHNeZxGLcn"},
  {"username": "Random-59", "wallet": "GBr3QtEvRJ85QtZ4TCjfv9rYYZrmLaUxdgqBNvYmMdz4"},
  {"username": "Random-60", "wallet": "FhtFNufrBVLaAJH1momEs2JASimPKFTqUGyfpKKmArvt"},
  {"username": "Random-61", "wallet": "5cqg2JtaHMNCN9hT3Bp6hEsfVn9e9S6BPuW6Qwftidbh"},
  {"username": "Random-62", "wallet": "2sNTcnKPwEGzjnZ3caqvvGsBqHdGemaowPHD7m4dwinV"},
  {"username": "Random-63", "wallet": "7nzEh7gCZwpr98CuBATuUYKRgpekc5xenAVyy2C7Tw2Y"},
  {"username": "Random-64", "wallet": "7CFXFm86qMTCmE3PTcicCx4EBEBti9DH78tankXfhZjq"},
  {"username": "Random-65", "wallet": "7Kvy2uSVxwjiWPBUMYTZ1XyqVKN92JDXZacyvmmfxaVv"},
  {"username": "Random-66", "wallet": "DTRSoTPSJL3JzH8Ne2m4o9iJEzrieB32vbNyTfsVSpAZ"},
  {"username": "Random-67", "wallet": "9ZkSq96MSwNgc3vKNDEAHgwsUcjVtMwrXmtLVE8LEgxr"},
  {"username": "Random-68", "wallet": "62oCLsp5zm94TYobwKgugMyCF1DnaJsSZBhz757Uzn7b"},
  {"username": "Random-69", "wallet": "BbJztKfsk86AgCXSmv7sqgsNuRBMAAUcqWJzxBFgdxvc"},
  {"username": "Random-70", "wallet": "9UJPeoZGYsek1ZFAB9rH65gh7w3xXgonJ5cD7D9gYb49"},
  {"username": "Random-71", "wallet": "HKYSwmwVraMCqtFbF5ZTinGUHu82gt18dBmdJSFVMrRC"},
  {"username": "Random-72", "wallet": "GVdCW8TDczHAjs4669bpZ4rMERmXk7mZx2Ld43mRZqkp"},
  {"username": "Random-73", "wallet": "GdtgKRUy2EVJX9QZKtw5ivWzs8w5Qbmqqo1bdmEdJRNB"},
  {"username": "Random-74", "wallet": "CW6twgqSdUjLQ1xU4LZGroW1s5aWajmEiG6mN6D3v2HB"},
  {"username": "Random-75", "wallet": "G3PwWfAS9pY5cNgxTxP8NG7b8sGzMbDGire6h4JKp7t8"},
  {"username": "Random-76", "wallet": "4wBgNRf5tXbYp2d2SsYrjotn36NyaWMu4LEbtbQTUK4c"},
  {"username": "Random-77", "wallet": "776kieHLn8ZhrbmwHymXFxEU3Tyhowjc95E7EcbTYKgL"},
  {"username": "Random-78", "wallet": "FH7tFfBhwVfJGkjeeydo3YrdTiX9MLdFVxhRBKVXfZjw"},
  {"username": "Random-79", "wallet": "5hKxrZiPLeapQXN13itsEwxFSwhdMnkxf59yGeXLSjJE"},
  {"username": "Random-80", "wallet": "CVTU4ZHvFj8MBfJRsHZ9aBUknTbk25JZc2LFvFxwsrKE"},
  {"username": "Random-81", "wallet": "3bkM3CMVqMfWgC4yyHrqAEs5exChb8mrBYQQ3aavVS81"},
  {"username": "Random-82", "wallet": "6vL5ZmHuE6ZLzxW3NSn5XkW8km62ig9VazRZm68dAjHE"},
  {"username": "Random-83", "wallet": "5B9dpNfbEdhrCzrCB7iK2t5mD1JD4bmZUnYoRQCrnGHM"},
  {"username": "Random-84", "wallet": "cFgsDmPPZ8jcmTEDWhre5nRPv8cxkQmUjBmKDraotu1"},
  {"username": "Random-85", "wallet": "BtXrhuR1A86duaP6uWTi6DvBKkkdNC7mNLaUUB3SW6sA"},
  {"username": "Random-86", "wallet": "AdQUTnThNZ1fk21ZHJwmAtRzWG7YAtbwy4nBJi56MXcV"},
  {"username": "Random-87", "wallet": "Gx6w7Ys5vW5mPYacs66jgnWFMg1Nzyxq78nE13CH3Ea8"},
  {"username": "Random-88", "wallet": "HgRnmwX8U9owhMc7pAPjeQ4TUGysDaHzRkPygF8nyKKk"},
  {"username": "Random-89", "wallet": "BkG7Ziok3rGnLMq5SKs18AEgd5rjNQr1Y7ffmnroEn3D"},
  {"username": "Random-90", "wallet": "21wm5fo5gDXXRYB8RNviwnhEmwWPodSWAsjFMurWWcHr"},
  {"username": "Random-91", "wallet": "2rPikcB2aWNYDVk8yamUkCDknkamWi11vbErrAMYfkUp"},
  {"username": "Random-92", "wallet": "67qhXgy5Xg4c334npJLTuZCJqCF9FXo6FErMKZNBNKmn"},
  {"username": "Random-93", "wallet": "265zx6633mhmRyb59cJwAssKU5r4Wyw4w5ZSmc5v8BkX"},
  {"username": "Random-94", "wallet": "AYUFpCnjLYcydpqZpdWz1Z3msCNx9f8S7jvUaTRRGf3n"},
  {"username": "Random-95", "wallet": "SK5HCGswSymtVJ6nAVt2Ba1RtwCfWFVDLD217fe7SdH"},
  {"username": "Random-96", "wallet": "5YdsHZTc2yeYdKfaC2Kj1tu1D1AnwYxnLsbicifG4WmU"},
  {"username": "Random-97", "wallet": "HRGFK66X2QZ2Y9FxQspnRY1sBG1dVpniX4pJWBrRtdUG"},
  {"username": "Random-98", "wallet": "CKji8LD38oCVAQ7nWKfjKzSFBdx3D5jaoY4kp3s1X9eB"},
  {"username": "Random-99", "wallet": "7QqFFHrMY4iLf3JHTfcvx4VKNdd3nDsdqfop3L6iTR93"},
  {"username": "Random-100", "wallet": "9UJVuGoXqq5rYJDq4WQSWXaKitnie2veV9GmqZME93Pa"},
]
    # Agar aur accounts hon toh aese add kar lein:
    # {"username": "apna_username_2", "wallet": "0xYourWalletAddressHere2"},


async def handle_modal(page):
    modal = page.locator("#scamMigrationWarningModal")
    try:
        if await modal.is_visible(timeout=5000):
            print("⚠️ Closing modal...")
            buttons = modal.locator("button")
            if await buttons.count() > 0:
                await buttons.first.click()
                await page.wait_for_timeout(1000)
    except:
        pass

async def run_bot():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"]
        )

        for acc in accounts:
            context = await browser.new_context()
            page = await context.new_page()

            print("Running account:", acc["username"])

            try:
                await page.goto("https://theros.io/prelaunch", timeout=80000)
                await page.wait_for_load_state("networkidle", timeout=15000)
            except TimeoutError:
                print(f"Timeout for {acc['username']}. Skipping.")
                await context.close()
                continue

            await handle_modal(page)
            await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            await page.wait_for_selector("input", timeout=15000)

            inputs = await page.query_selector_all("input")
            if len(inputs) < 2:
                print(f"Not enough inputs for {acc['username']}, skipping")
                await context.close()
                continue

            await inputs[0].fill(acc["username"])
            await inputs[1].fill(acc["wallet"])

            if len(inputs) > 2:
                await inputs[2].fill("bot")

            await handle_modal(page)

            create_btn = page.locator("#registerBtn")
            try:
                await create_btn.click(timeout=9000)
            except TimeoutError:
                await create_btn.click(force=True)

            next_btn = page.locator("#nextQuestionBtn")
            try:
                await next_btn.wait_for(state="visible", timeout=8000)
                await next_btn.click()
            except:
                pass

            answer_selector = f"#answer{ANSWER.upper()}"
            try:
                await page.locator(answer_selector).click(timeout=20000)
                print("Answered:", ANSWER)
            except Exception as e:
                print(f"Failed to answer: {e}")

            await context.close()

        await browser.close()
        print("🎉 All accounts processed successfully!")

if __name__ == "__main__":
    asyncio.run(run_bot())
  

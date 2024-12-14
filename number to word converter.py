def number_to_words(n):
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
    teens = ["Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    if n == 0:
        return "Zero"
    elif 1 <= n <= 10:
        return ones[n]
    elif 11 <= n <= 19:
        return teens[n - 11]
    elif 20 <= n <= 99:
        return tens[n // 10] + (" " + ones[n % 10] if n % 10 != 0 else "")

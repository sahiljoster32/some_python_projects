import requests
import sys
import hashlib
# "_" -> current value`s no use in function

# this for getting the respone .........................
def data_geter(query, _):
    url = "https://api.pwnedpasswords.com/range/" + f"{query}"
    response = requests.get(url)
    return data_reader(response, _)


# this for reading the response .......................
def data_reader(data_response, _):
    text_form_ = data_response.text
    list_line_wise = text_form_.split("\n")
    new_list_column_wise = [parse.split(":") for parse in list_line_wise]
    # print(new_list_column_wise)
    return Compare_hashed_values(new_list_column_wise, _)

# this for converting the stringed password to hashed value with sha-1 algorithm.................
def password_to_hashed(password):
    hashed_password = hashlib.sha1(password.encode("utf-8"))
    hashed_value = (hashed_password.hexdigest()).upper()
    first5_chars, tail_of_hashed = hashed_value[:5], hashed_value[5:]
    return data_geter(first5_chars, tail_of_hashed)

# to compare the values ................
def Compare_hashed_values(hashed_list, hashed_to_with_compare):
    for hashed, count in hashed_list:
        if hashed == hashed_to_with_compare:
            return count
    return 0

# to read arguments ...................... and give output in same ...............
def main(values):
    for item in values:
        count = password_to_hashed(item)
        if count != 0:
            print(f"---------------{item} was found-----------------") 
            print(f"{count}")
            print("times ... you should change your password\n\n")
        else:
            print(f"************************yeah your password {item} is never appear in breacher's set************************\n")
    return "Now, you know where to go!!!"

# this function is for taking arguments from terminal -----------
# 1st function --------------------------------------------------
if __name__ == "__main__":
    list_argument = sys.argv[1:]
    main(list_argument)

#this function is for taking passwords from text or anyother readable format file-------------
# 2nd function -------------------------------------------------------------------------------
if __name__ == "__main__":
    with open(r"-----------------------your path is here --------------------", "r") as password_file:
        text_pass = password_file.read()
        split_pass = text_pass.split(" ")
        main(split_pass)

# always use absolute path rather than relative path-----------------
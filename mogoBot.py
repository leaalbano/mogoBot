import praw

#Submissions we reply to must contain LF or HAVE
REQUEST = ["LF", "LF:", "HAVE", "HAVE:"]

def main():
    #reddit instance
    reddit = praw.Reddit(
        client_id="17jlOisn-5oCfbnlSxO0ng",
        client_secret="sJIpnyR1gOBjKXg3D71NEHodl4MRVA",
        user_agent="TRADE (by u/mogoBot)",
        password="Fullerton30!",
        username="mogoBot"
    )
    #The subreddit we want to iterate through
    subreddit = reddit.subreddit("MonopolyGoTrading")
    for submission in subreddit.stream.submissions():
        trade_bot(reddit, subreddit, submission)

def trade_bot(reddit, subreddit, submission):
    print("Starting trade_bot function...")
    processed_request = False  # Flag to track if a request type has been processed for this submission
    submission_body = submission.selftext
    for request_type in REQUEST:
        if request_type in submission_body:
            request_type, sticker_name = extract_info(submission_body)
            mapped_request_type = map_request_type(request_type)
            matching_submissions = fetch_matching_submissions(mapped_request_type, sticker_name, subreddit)
            reply_to_submission(submission, matching_submissions)
            processed_request = True
            break

    return None, None

def extract_info(submission_body):
    '''Extract request type and sticker name from the submission body'''
    parts = submission_body.split()
    # Initialize request_type and sticker_name
    request_type = None
    sticker_name = None

    # Iterate through the parts to find the request type
    for i, word in enumerate(parts):
        if word.startswith("LF") or word.startswith("HAVE"):
            # Found the request type
            request_type = word
            # Index of the request type in parts
            request_type_index = parts.index(request_type)
            # Extract sticker_name as the remaining part of the submission_body
            sticker_name = ' '.join(parts[request_type_index + 1:])
            break

    # If request_type is found, return it along with sticker_name
    if request_type:
        print(f"Request Type: {request_type}, Sticker Name: {sticker_name}")
        return request_type, sticker_name
    else:
        print(submission_body)
        # If no request type is found, return None values
        return None, None
    
def map_request_type(request_type):
    '''Map LF: to HAVE: and vice versa'''
    if request_type is not None:
        request_type = request_type.upper()
    if request_type == "LF" or request_type == "LF:":
        match_request = "HAVE"
        print(f"Request type: {request_type}. Seeking request type: {match_request}")
        return match_request
    elif request_type == "HAVE" or request_type == "HAVE:":
        match_request = "LF"
        print(f"Request type: {request_type}. Seeking request type: {match_request}")
        return match_request
    else:
        print("Unknown req type: ", request_type)
        return None

def fetch_matching_submissions(match_request, sticker_name,subreddit, limit=None, max_submissions=3):
    #Fetch the 3 newest submissions containing the specified request type and sticker name.
    matching_submissions = []
    matching_submissions_count = 0
    for submission in subreddit.new(limit=limit):
        #looks at every submission even past 'load more submissions'
        #submission.submissions.replace_more(limit=5)
        #for submission in submission.submissions.list():
        #match 
        if match_request.lower() in submission.selftext.lower() and sticker_name.lower() in submission.selftext.lower():
            
            submission_info = (submission.selftext, submission.author.name, submission.permalink)
            matching_submissions.append(submission_info)
            matching_submissions_count += 1
            
            if matching_submissions_count >= max_submissions:
                print(f"Here are the suggested trades: {matching_submissions}")
                break
    return matching_submissions

def reply_to_submission(submission, matching_submissions):
    # Reply to the original submission with the matching submissions
    reply_text = "Here are the potential trades I found for you:\n\n"
    #link = permalink
    for trade_info in matching_submissions:
        trade_description, username, link = trade_info
        formatted_trade = f"u/{username} \'{trade_description}' ({link})\n"
        reply_text += formatted_trade + "\n"

    if reply_text:
        submission.reply(reply_text)
    else:
        print("Reply text is empty. No comment will be posted.")

if __name__ == "__main__":
    main()

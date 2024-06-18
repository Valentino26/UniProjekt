import customtkinter as ctk
from testing import main
from tweet_poster import post_tweet
from GenTweet import return_tweet

# Initialize the customtkinter app
app = ctk.CTk()
app.title("News Categories")
app.geometry("1256x600")

selected_article = {"title": "", "summary": ""}

# Confirm that you want to generate tweet button
def confirm_generate_tweet(title, summary):
    selected_article['title'] = title
    selected_article['summary'] = summary

    #initalize new window attached to app main window
    confirm_window = ctk.CTkToplevel(app)
    confirm_window.title("Confirm Tweet Generation")
    confirm_window.geometry("800x300")
    
    #Label for title of news-article
    title_label = ctk.CTkLabel(confirm_window, text=f"Title: {title}", font=("Arial", 14, "bold"))
    title_label.pack(pady=10)
    
    #Label for summary of news-article
    summary_label = ctk.CTkLabel(confirm_window, text=f"Summary: {summary}", font=("Arial", 12))
    summary_label.pack(pady=10)
    
    #Button to theoretically generate tweet, won't actually work since you have to provide your API key, etc. in the tweet poster file
    tweet_button = ctk.CTkButton(confirm_window, text="Generate Tweet", command=generate_tweet)
    tweet_button.pack(pady=20)
    
#Generate a political tweet, basically just a summary of the top news articles
def generate_tweet():
    #Create tweet window attached to app main window
    tweet_window = ctk.CTkToplevel(app)
    tweet_window.title("Generated Tweet")
    tweet_window.geometry("800x300")
    
    #Generate tweet label
    tweet = f"Title: {selected_article['title']}\nSummary: {selected_article['summary']}"
    tweet_label = ctk.CTkLabel(tweet_window, text=tweet, font=("Arial", 12))
    tweet_label.pack(pady=10)
    
    #Post button, opens confirm post window
    post_button = ctk.CTkButton(tweet_window, text="Post Tweet", command=lambda: confirm_post_tweet(tweet))
    post_button.pack(pady=10)
    
# Confirm that you actually want to post this
def confirm_post_tweet(tweet):
    #Initialize attached window
    confirm_window = ctk.CTkToplevel(app)
    confirm_window.title("Confirm Posting")
    confirm_window.geometry("800x300")
    
    #Initialize label
    confirm_label = ctk.CTkLabel(confirm_window, text="Do you want to post this tweet?", font=("Arial", 14))
    confirm_label.pack(pady=10)
    
    #Initialize post button
    post_button = ctk.CTkButton(confirm_window, text="Yes", command=lambda: post_tweet_and_confirm(tweet, confirm_window))
    post_button.pack(pady=10)
    
    #Initialize cancel button
    cancel_button = ctk.CTkButton(confirm_window, text="No", command=confirm_window.destroy)
    cancel_button.pack(pady=10)

# Post tweet and confirm, that it was successfully posted
def post_tweet_and_confirm(tweet, window):
    post_tweet(tweet)
    window.destroy()
    success_window = ctk.CTkToplevel(app)
    success_window.title("Success")
    success_window.geometry("800x300")
    
    success_label = ctk.CTkLabel(success_window, text="Tweet posted successfully!", font=("Arial", 14))
    success_label.pack(pady=10)
    
    close_button = ctk.CTkButton(success_window, text="Close", command=success_window.destroy)
    close_button.pack(pady=10)

# Display the articles on the main page after clicking on the political button
def display_political_articles():
    articles = main()
    political_button.pack_forget()
    personal_button.pack_forget()
    
    articles_frame = ctk.CTkFrame(app, width=750, height=400, corner_radius=10)
    articles_frame.pack(pady=20)
    
    #Picks the top three articles and displays them in order
    for article in articles[:3]:
        article_frame = ctk.CTkFrame(articles_frame, width=700, height=150, fg_color="grey")
        article_frame.pack(pady=10, padx=10, fill="both", expand=True)
        
        title_label = ctk.CTkLabel(article_frame, text=article['title'], font=("Arial", 14, "bold"), fg_color="darkgrey")
        title_label.pack(fill="x", pady=(5, 0))
        
        summary_label = ctk.CTkLabel(article_frame, text=article['summary'], font=("Arial", 12), fg_color="grey")
        summary_label.pack(fill="x", pady=(0, 5))
        
        generate_tweet_button = ctk.CTkButton(article_frame, text="Generate Tweet", 
                                              command=lambda t=article['title'], s=article['summary']: confirm_generate_tweet(t, s))
        generate_tweet_button.pack(side="right", pady=(0, 5), padx=(0, 5))

#generates a personal tweet using HuggingChat 
def generate_personal_tweet():
    tweet_page = ctk.CTkToplevel(app)
    tweet_page.geometry("600x200")

    title_tweet = ctk.CTkLabel(tweet_page, text="This is your tweet", font=("Arial", 14, "bold"), fg_color="darkgrey")
    title_tweet.pack(fill="x", pady=(0, 5))

    tweet = return_tweet()
    print(f"Extracted tweet: {tweet}")  # Debug statement

    # Ensure the tweet is not None or empty
    if tweet:
        display_tweet = ctk.CTkLabel(tweet_page, text=tweet, font=("Arial", 12), fg_color="grey")
        display_tweet.pack(fill="x", pady=(0, 5))
    else:
        display_tweet = ctk.CTkLabel(tweet_page, text="No tweet generated.", font=("Arial", 12), fg_color="grey")
        display_tweet.pack(fill="x", pady=(0, 5))

# Display the personal section, once button was clicked
def display_personal_section():
    political_button.pack_forget()
    personal_button.pack_forget()
    
    personal_frame = ctk.CTkFrame(app, width=750, height=400, corner_radius=10)
    personal_frame.pack(pady=20)
    
    tweet_generate_button = ctk.CTkButton(personal_frame, text="Generate Tweet", command=generate_personal_tweet)
    tweet_generate_button.pack(side="right", pady=(0, 5), padx=(0, 5))


# Create Political button
political_button = ctk.CTkButton(app, text="Political", command=display_political_articles)
political_button.pack(pady=20)

# Create Personal button
personal_button = ctk.CTkButton(app, text="Personal", command=display_personal_section)
personal_button.pack(pady=20)

# Run the app
app.mainloop()

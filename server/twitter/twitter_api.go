package twitter_api

import (
	"encoding/json"
	"log"

	twitter "github.com/dghubble/go-twitter/twitter"
	"github.com/dghubble/oauth1"
)

type TwitterClient struct {
	client *twitter.Client
}

func Init(consumer string, secret string, access string, access_secret string) *TwitterClient {

	if consumer == "" || secret == "" || access == "" || access_secret == "" {
		log.Panic("Not all .env variables are not defined.")
	}

	config := oauth1.NewConfig(consumer, secret)
	token := oauth1.NewToken(access, access_secret)
	httpClient := config.Client(oauth1.NoContext, token)
	client := twitter.NewClient(httpClient)

	return &TwitterClient{
		client: client,
	}
}

func (twitterClient *TwitterClient) SearchTweets(query string) string {
	search, resp, err := twitterClient.client.Search.Tweets(&twitter.SearchTweetParams{
		Query: query,
	})

	if err != nil {
		log.Panic(err)
	}

	var result string

	if resp.StatusCode == 200 {
		byteArray, err := json.Marshal(search)

		if err != nil {
			log.Panic(err)
		}

		result = string(byteArray)
	}

	defer resp.Body.Close()

	return result
}

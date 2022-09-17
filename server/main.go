package main

import (
	"log"
	"os"

	go_router "github.com/LegationPro/routes"
	twitter_api "github.com/LegationPro/twitter"
	"github.com/gin-gonic/gin"
	"github.com/joho/godotenv"
)

func main() {
	err := godotenv.Load()

	if err != nil {
		log.Panic(err)
	}

	consumer := os.Getenv("consumer-key")
	consumer_secret := os.Getenv("consumer-secret")
	access_token := os.Getenv("access-token")
	access_token_secret := os.Getenv("access-token-secret")

	twitterBot := twitter_api.Init(
		consumer,
		consumer_secret,
		access_token,
		access_token_secret,
	)

	engine := gin.Default()

	routeHandler := go_router.Start(engine)
	routeHandler.ActivateTwitterAPI(twitterBot)
	engine.Run("localhost:4050")
}

package go_router

import (
	"net/http"

	twitter_api "github.com/LegationPro/twitter"
	"github.com/gin-gonic/gin"
)

type RouteHandler struct {
	engine *gin.Engine
}

type TwitterRestAPI struct {
	routeHandler *RouteHandler
}

func (twitter_rest_api *TwitterRestAPI) implGetTweets(twitterBot *twitter_api.TwitterClient) {
	twitter_rest_api.routeHandler.engine.GET("/tweets/:query", func(c *gin.Context) {
		query := c.Param("query")
		data := twitterBot.SearchTweets(query)
		c.IndentedJSON(http.StatusOK, data)
	})
}

func Start(engine *gin.Engine) *RouteHandler {
	return &RouteHandler{
		engine: engine,
	}
}

func (routeHandler *RouteHandler) ActivateTwitterAPI(twitterBot *twitter_api.TwitterClient) {
	// TODO: API

	twitterRestApi := TwitterRestAPI{
		routeHandler: routeHandler,
	}

	twitterRestApi.implGetTweets(twitterBot)
}

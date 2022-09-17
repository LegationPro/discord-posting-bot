package go_server

import (
	"github.com/gin-gonic/gin"
)

func Run(addr string) *gin.Engine {
	r := gin.Default()
	return r
}

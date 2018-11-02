#!/usr/bin/Rscript --vanilla

library(lattice, verbose=FALSE)

data <- data.frame(x1=NULL, x2=NULL, y=NULL, label=NULL)

sphere <- function(data=data) {
	return(data$x1^2+data$x2^2)
}

rosenbrock <- function(data=data) {
	return((1-data$x1)^2 + 100 * (data$x2-(data$x1)^2)^2)
}

step <- function(data=data) {
	return(floor(data$x1) + floor(data$x2))
}

quartic <- function(data=data) {
	return((data$x1^4+2*data$x2^4)+rnorm(length(data$x1),0,1))
}

######
# Esfera
#####
x1 <- seq(from=-5.12, to=5.12, length=50)
x2 <- seq(from=-5.12, to=5.12, length=50)
g <- expand.grid(x1=x1, x2=x2)

g$label <- rep("Sphere", length(g))
g$y <- sphere(data=g)
g$y <- g$y/max(g$y)
data <- rbind(data, g)

g <- NULL
x1 <- NULL
x2 <- NULL

# Rosenbrock
x1 <- seq(from=-2.048, to=2.048, length=50)
x2 <- seq(from=-2.048, to=2.048, length=50)
g <- expand.grid(x1=x1, x2=x2)

g$label <- rep("Rosenbrock", length(g))
g$y <- rosenbrock(data=g)
g$y <- g$y/max(g$y)

data <- rbind(data, g)
g <- NULL
x1 <- NULL
x2 <- NULL

# Step
x1 <- seq(from=-5.12, to=5.12, length=50)
x2 <- seq(from=-5.12, to=5.12, length=50)
g <- expand.grid(x1=x1, x2=x2)

g$label <- rep("Step", length(g))
g$y <- step(data=g)
g$y <- g$y/max(g$y)

data <- rbind(data, g)
g <- NULL
x1 <- NULL
x2 <- NULL


# Quartic
x1 <- seq(from=-1.28, to=1.28, length=50)
x2 <- seq(from=-1.28, to=1.28, length=50)
g <- expand.grid(x1=x1, x2=x2)

g$label <- rep("Quartic function with noise", length(g))
g$y <- quartic(data=g)
g$y <- g$y/max(g$y)

data <- rbind(data, g)
g <- NULL
x1 <- NULL
x2 <- NULL

#print(g)
x11()
#wireframe(y ~ x1 + x2 | label, data=data, zlim=c(-10,20), shade=TRUE, scales=list(relation="free",arrows=FALSE))

myprepanel <- function( ...) {
	return(lattice.getOption("prepanel.default.wireframe"))
}

wireframe(y ~ x1 + x2 | label, data=data, 
	scales=list(relation="free"), shade=TRUE,
	prepanel = myprepanel())
##wireframe(E ~ mu + sigma | m, data=g, shade=TRUE, scales = list(arrows=FALSE))
dev.copy2eps(file="../figs/deJong.eps");
while (1) Sys.sleep(10)

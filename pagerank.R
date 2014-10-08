M <- t(matrix(c(0,0,0,0.5,0,0,0.5,1,1),nrow=3,ncol=3))

beta <- 0.7
jump <- 0.3 / 3
r <- c(1/3, 1/3, 1/3)

while(FALSE){
  cat(r,"\n")r
  r <- beta * M %*% r + jump
  cat(r,"\n")
}

M2 <- t(matrix(c(0,0,1,0.5,0,0,0.5,1,0),nrow=3,ncol=3))
r2 <- c(1, 1, 1)
beta2 <- 0.85
jump2 <- 0.15 / 3
for(i in 1:5){
  r2 = M2 %*% r2
  cat(i," ",r2,"\n")
  
}
## sample data
library(getopt)
arg = getopt(matrix(c(
'input', 'i', 1, "character"
), byrow=TRUE, ncol=4))


input <- arg$input
sample <- read.csv(input)
length(unique(sample[,1]))
if(dim(sample)[2]<3){
  h <- sample[,2]
}else{
  h <- apply(sample[,-1], 1, mean)
}
print("1")
names(h) <- seq(1,length(sample[,1]),1)
hc <- {}
for(n in 1:length(as.character(unique(sample[which(duplicated(sample[,1])=="TRUE"),1])))){
  g1 <- h[which(as.character(sample[,1])==as.character(unique(sample[which(duplicated(sample[,1])=="TRUE"),1]))[n])]
  hc[n] <- names(which(g1==max(g1)))
}
sample_fi <- sample[-which(sample[,1]%in%sample[hc,1]),]
length(unique(sample_fi[,1]))

sample_fi <- rbind(sample[hc,],sample_fi)
length(unique(sample_fi[,1]))

MF <- read.csv("Pre.reference.csv")
## select genes both in sample matrix and reference matrix ====
im_ref <- MF[which(MF[,1]%in%sample_fi[,1]),]
sample_ref <- sample_fi[which(sample_fi[,1]%in%im_ref[,1]),]

im_ref <- im_ref[order(im_ref[,1]),]
sample_ref <- sample_ref[order(sample_ref[,1]),]
write.csv(im_ref,"Reference.csv",row.names = F)
write.csv(sample_ref,"Sample.csv",row.names = F)


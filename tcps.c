#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#define PORT 8080

int main()
{
  int sf;
  sf = socket(AF_INET,SOCK_STREAM,0);
  
  struct sockaddr_in ad;
  memset(&ad,0,sizeof(ad));
  
  ad.sin_family = AF_INET;
  ad.sin_port = htons(PORT);
  ad.sin_addr.s_addr = INADDR_ANY;
  
  bind(sf,(struct sockaddr*)&ad,sizeof(ad));
  
  listen(sf,3);
  
  int ns,n,d=0;
  n = sizeof(ad);
  ns=accept(sf,(struct sockaddr*)&ad,(socklen_t*)&n);  
  
  read(ns,&d,sizeof(d));
  int f=1;
  for(int i=1;i<=d;i++)
   f=f*i;
   
  send(ns,&f,sizeof(f),0);
  //printf("%d",f);
  
  close(ns);
  close(sf);
  
}

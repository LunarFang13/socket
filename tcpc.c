#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <stdio.h>
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
  
  connect(sf,(struct sockaddr*)&ad,sizeof(ad));
  
  int d;
  printf("Enter number/n");
  scanf("%d",&d);
  send(sf,&d,sizeof(d),0);
  
  read(sf,&d,sizeof(d));
  printf("%d",d);
  
  close(sf);
}

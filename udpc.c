#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <string.h>
#include <netinet/in.h>
#define PORT 8080

int main()
{
  int sf;
  sf = socket(AF_INET,SOCK_DGRAM,0);
  
  struct sockaddr_in ad;
  memset(&ad,0,sizeof(ad));
  
  ad.sin_port = htons(PORT);
  ad.sin_family = AF_INET;
  ad.sin_addr.s_addr = INADDR_ANY;
  
  bind(sf,(struct sockaddr*)&ad,sizeof(ad));
  
  int n=sizeof(ad);
  int d=0,an=0;
  printf("Enter acct number\n");
  scanf("%d",&an);
  printf("Enter amt to withdraw\n");
  scanf("%d",&d);
  sendto(sf,&d,sizeof(d),0,(struct sockaddr*)&ad,sizeof(ad));
  recvfrom(sf,&d,sizeof(d),0,(struct sockaddr*)&ad,(socklen_t*)&n);
  printf("Balance =%d",d);
  
  close(sf);
}


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#define PORT 8080

int main()
{
  int sf;
  sf = socket(AF_INET,SOCK_DGRAM,0);
  
  struct sockaddr_in ad,a;
  memset(&ad,0,sizeof(ad));
  memset(&ad,0,sizeof(a));
  
  ad.sin_port = htons(PORT);
  ad.sin_family = AF_INET;
  ad.sin_addr.s_addr = INADDR_ANY;
  
  bind(sf,(struct sockaddr*)&ad,sizeof(ad));
  
  int n= sizeof(a);
  int d;
  recvfrom(sf,&d,sizeof(d),0,(struct sockaddr*)&a,(socklen_t*)&n);
  int amt = 1000 - d;
  sendto(sf,&amt,sizeof(amt),0,(struct sockaddr*)&a,n);
  
  
  close(sf);
}

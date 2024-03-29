---
layout: post
title:  "[코포] Codeforces Round#766 후기"
date:   2022-01-16 15:15:00 +0900
categories: blog_old
tags: Codeforces 코포후기
use_math: true
---

지난 밤 Div.2 라운드가 있어서 오랜만에 참가해보았다. 문제 난이도 구성이 딱 나한테 유리했다는 느낌이 들었는데(ㅎㅎ) 덕분에 A,B,C 풀어서 3솔하고 처음으로 블루를 달았다!! 

| ![Codeforce_Result](/assets/images/codeforce_blue.png#center) | 
|:--:| 
| 만세! |

### 문제별 후기
[공식 에디토리얼](https://codeforces.com/blog/entry/99067)

라운드 공지가 나중에 찾기 은근히 귀찮으니까 여기에 일단 저장해두고~

#### A. Not Shading
$n \times m$ 격자칸이 흑 또는 백으로 칠해져있고, 어떤 검은 칸을 골라 같은 행을 모두 검게하거나, 같은 열을 모두 검게하는 operation을 할 수 있다. 임의의 $(r,c)$ 를 검게하는데 필요한 operation의 수를 구하는 문제이다.

가끔은 A부터 오잉??하는 문제들이 나오곤 했는데, 이번엔 망설임 없이 3분컷 했다.
1. 이미 검으면 0번
2. 1이 아닌데 같은 행 또는 같은 열에 검은칸이 있으면 1번
3. 1, 2가 아닌데 검은 칸이 있기는 하면 2번
4. 검은 칸이 전혀 없으면 -1

간단하다!

#### B. Not Sitting
$n \times m$ 격자칸이 있고, 사람 A가 그 중 $k$개 칸을 핑크색으로 칠하면, B가 핑크색이 아닌 칸 중 하나에 앉는다. 그 다음 A는 B가 앉지 않은 아무 칸이나 앉는다. B는 A와 최대한 가까이 앉고 싶고, A는 B와 최대한 멀리 떨어지고 싶다. A,B 모두 최선의 선택을 할 때, 가능한 모든 $k$, 즉 $k=0,1,2,...,nm-1$에 대해서 거리를 구하는 문제이다.

이 문제는 보고 나서 아이디어가 바로 떠오르지는 않았다. 어디에 칠하고 어디에 앉지? 하는 생각을 하다보면 꼬이기 쉽상이다. 문제를 반절만 떼어서 거꾸로 생각했더니 풀이를 떠올릴 수 있었다.

B가 앉아있는 자리가 주어졌을 때 A는 어디에 앉아야 할까? 당연히 네 귀퉁이 중 하나일 것이다. 그렇다면 B는 어디에 앉아야 거리를 최소화 할 수 있을까? 네 귀퉁이까지의 거리 중 최대가 최소가 되는 곳이다. 그렇다면 A는 가장 먼저 그런 곳부터 핑크색으로 칠해야 할 것이다.

여기까지 떠올렸다면 그 다음은 구현이다. 에디토리얼에서는 거의 one-liner로 깔쌈하게 구현했지만, 나는 각 $(r,c)$에 대해 네 귀퉁이 까지의 거리 $abs(r-0)+abs(c-0), abs(r-(n-1))+abs(c-0), ... , abs(r-(n-1))+abs(c-(m-1))$ 중 최대인 값을 구한 뒤 저장해 두었다가, 정렬해서 출력했다.

여기까지 18분을 사용했다.

#### C. Not Assigning
Vertex n개 짜리 tree가 주어진다. 여기에 원하는 대로 weight를 부여하는 문제인데, edge 1개 혹은 2개짜리 path를 생각했을 때 그 길이가 소수(prime)여야 한다. 불가능하면 -1을 출력한다.

이 문제는 구현에 좀 애를 먹었다. 예제 테케에 불가능한 경우가 오픈되어있어서, 한 vertex에 3개 이상의 edge가 연결되면 안됨은 쉽게 발견했다. 2가 유일한 짝수 소수이므로, edge 3개에 닿아있는 vertex에서 edge 2개짜리 path를 따져보면 무조건 소수가 아닌게 생기게 된다.

지금 보니 이 문제 푸는데 37분이 걸렸는데, 구현을 좀 더 빨리 할 수 있었으면 레이팅을 더 올릴 수 있었을 것 같아서 아쉽기도 하다. 입력받은 edge 순서대로 weight를 출력해야 하는데, 자꾸 머릿속에서 edge번호와 vertex 번호가 헷갈리면서 구현이 자꾸 꼬였다. 지금 생각해보면 코드를 좀 더럽게 짠것 같은데, 어쨌든 꾸역꾸역 짜서 맞았다. 최근에 트리 관련된 문제를 거의 못풀었던 것 같은데, 더 연습해야겠다.

#### D, E, F (못 풀음)
D번의 문제는 대충...

$10^6$ 이하의 서로다른 양의 정수를 $10^6$개 이하 담고있는 array에서, 원한다면 아무거나 두 개 골라 둘의 최대공약수를 추가할 수 있다. 단, 이미 있는 건 추가가 안된다. 주어진 array에서 최대 몇개가 새로 추가될 수 있는지 구하는 문제이다.

$n \le 10^6$ 조건을 보고 대충 array 돌면서 $O(logn)$ 연산을 해서 $O(nlogn)$에 푸는 문제이겠다, 하는 건 알았는데, 도대체 어떤 규칙으로 추가가 되고 안되는 건지 감을 못잡았다. 이것도 아이디어만 떠올렸으면 구현은 5분컷 했을 텐데 아쉽다. 더 공부하자 ㅜㅜ.

E번은 격자칸 왼쪽 아래 끝에서 오른쪽 위 끝으로 가는 최단 경로를 찾는 문제이되, 각 층마다 좌우로 움직이는데에는 cost가 주어져있고 위로 움직이는 것은 주어진 '사다리'에서만 가능한 문제 설정이었다. D가 아무리 해도 안떠올라서 E를 보았는데, 엥? 날먹 DP네! 하고 이거를 좀 공략해보려 했다. 근데 $n,m$이 각각 최대 $10^5$이라 $(O(nm))$에는 택도 없는 문제임을 곧이어 깨달았다. 에라이~

F번은... 훑어만 보았다. 2750짜리 문제를 어떻게 풀어 ㅎㅎ

### 여담
내가 짠 비루한(?)) 코드는 [여기](https://github.com/SeminKim/Problem-Solving/tree/master/Codeforces/220115%20Round%20766)에 있다.

이번으로 벌써 17번째 코포였는데, 아직 갈 길이 멀다고 느끼지만 그래도 처음 시작했을 때보다는 많이 실력이 늘어난 것 같아 기쁘다. 옛날에는 Div.2 C번 푸는게 그렇게 소원이었는데, 요즘은 꽤 높은 확률로 푸는 것 같다(이번에는 C가 다른 때보다 쉽게 나왔지만😋).
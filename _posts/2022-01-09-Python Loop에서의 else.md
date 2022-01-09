---
layout: post
title:  "Python Loop에서의 else"
date:   2022-01-09 22:30:00 +0900
categories: Programming
tags: Python 
---

### 서론
>Python에서 ```if``` 없이 사용하는 ```else```키워드를 본 적 있는가?

뭐... 있다고 답하면 좀 민망하지만 일단 나는 없다! 고등학생 때부터 시작해서 수 년간 Python으로 코딩했지만 이런 건 여태 듣도 보도 못했다.

---
```
def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)
```

Code from: [Python documentation]("https://docs.python.org/ko/3/library/itertools.html")

---
위 코드는 ```itertools``` 모듈의 documentation인데, 꽤 자주 사용하게 되는 combinations() 항목의 설명에 적혀있는 내용이다. ```iterable```에서 ```r```개를 선택한 튜플을 반환해주는 generator가 어떻게 작동하는지 설명하는 부분이다.

코드 중간 While문 안에 ```for...else```구조가 보인다. 오늘의 주제는 이거다.
### 어....이게 무슨 뜻이지?
짧게 설명하자면: iteration이 모두 끝나면서 정상종료되면 else문이 실행되고, 중간에 ```break```나 ```return```등으로 종료되면 실행되지 않는다.

... 사실 이 부분은, 구글링하면 설명해둔 글이 꽤 있다. ```while```문에도 사용하여 루프 조건문이 false가 될때 실행하게 할 수도 있고, ```try...except...else```로 사용할 수도 있다. 못 믿겠다면, 지금 실험해보라!

### 어떻게 쓰지?
역시나 [스택오버플로우]("https://stackoverflow.com/questions/9979970/why-does-python-use-else-after-for-and-while-loops")에 좋은 답변이 있어서 슬쩍해왔다. ```objects``` 리스트에서 ```obj```를 찾는 코드를 생각해보자.
```
found_obj = None
for obj in objects:
    if obj.key == search_key:
        found_obj = obj
        break
else:
    print('No object found.')
```
찾아서 ```break```가 되면 만사OK고, 못찾으면 ```else```문을 실행한다. 뭐 간단해 보인다.

```
found_obj = None
flag = False
for obj in objects:
    if obj.key == search_key:
        found_obj = obj
        flag = True
        break
if flag is False:
    print('No object found.')
```
```for...else```를 사용하지 않고, 이렇게 flag를 세운 뒤 검사하는 걸 생각해보면?? 오~ 꽤 편리해 보인다. 키보드로 타이핑하는 한글자 한글자가 귀찮은 프로그래머들 취향저격이다.

### 근데 왜?
잠깐! 다시 처음으로 돌아가서 생각해보자. 처음 코드를 읽었을 때, 이 ```for...else```구조가 무슨 의미인지 바로 유추되던가? 나에게는 아니었다. 코드가 좀 간결해지기는 장점은 있지만, 코드를 처음 읽어보는 사람에게 낯설게 느껴진다면 결코 좋은 문법은 아니라 생각한다. 왜 ```if...else```에 이미 할당 되어있는 ```else```키워드를 여기에도 쓰게 해둔걸까?

문법 자체를 설명하는 글은 구글링하면 이미 꽤 있지만, 이 *왜?*를 설명하는 글은 국문으로 된 것이 없는 것 같아 여기에 좀 정리해보고 싶었다. 아까의 스택오버플로우 글에 이어지는 내용인데,

1. 이 문법은 귀도 행님이 아니라 크누스 행님이 고안한 것이었으며,
2. 당시에는 사람들이 for문을 보면 자연스럽게 if와 GOTO로 이루어진 블록을 생각했으므로 else를 사용하는 것이 자연스러웠고,
3. 지금보니 ```nobreak```같은 다른 키워드를 썼다면 헷갈리지 않았을 것

이란다. 영어로 직접 들어보고 싶다면 [유튜브]("https://youtu.be/OSGv2VnC0go?t=950")에 가서 살펴보자. 

### 그래서...
개인적으로는 키워드를 저렇게 abusing한 것은 마음에 들지는 않는다. 내가 처음 저 구조를 본 것이 Python documentation이었기 때문에 이게 되나? 하고 찾아보게 되었지, 인터넷에 떠도는 코드였다면? 그냥 indentation 오류인가, 하고 넘겼을 것이다. ```if```에 ```else```가 대응되는 구조는 아름답다. ```for```에 ```else```? 솔직히 말하면, 끔찍하다.

다만 코드가 간결해지는 장점도 분명 있기 때문에 앞으로 저런 상황을 마주하게 되면 나도 종종 사용하게 될 것 같다. 하위호환성을 생각하면 쉽게 버릴 수 없기도 하다.

그러나 많은 사람들과 같이 보는 코드에는 지양하는게 좋겠다. 나는 C++이나 Java와 같은 언어에 익숙하지 않지만, 대부분의 경우 이미 작성된 코드를 어렵지 않게 읽을 수 있다. *Syntax*를 익히는데는 시간이 걸려도, *Semantics*는 얼마든지 추론해볼 수 있다. 그런데 ```for...else```구조는 python에 익숙하지 않은 사람들에게는 직관적이지 않을 것 같다. 그런 면에서, ```for...else```는 꽤 쓸모있는 syntatic sugar지만 별로 좋은 문법은 아니라고 생각한다.

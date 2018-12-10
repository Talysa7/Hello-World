# filter
def even( a ) :
    return a%2 == 0
lst = range( 10 )
print( list( filter( even, lst ) ) )

print( list( filter( lambda a : a%2==1, range( 10 ) ) ) )


# map
b = list( range(10) )
print( b )

print( list( map( lambda a : a*2, [1, 2, 3, 4, 5] ) ) )
print( list( map( lambda a : a, "ABCDEF" ) ) )

msg = '''한국은행이 1년 만에 기준금리를 종전 연 1.50%에서 0.25%p 인상한 연 1.75%로 결정한 가운데, 이주열 한국은행 총재는 금융불균형 확대를 막기 위한 방안이었다고 의견을 밝혔다.
가계부채 증가 속도 등을 미뤄봤을 때 현 수준의 기준금리를 유지할 경우, 금융안정리스크까지 확대될 수 있다는 것이다.
이주열 총재는 국내 경제 성장 경로가 잠재성장율을 벗어난 것은 아니지만, 대외리스크나 기업가 심리 위축으로 내년 경기가 둔화될 우려가 있다고 진단했다.
30일 서울 중구 세종대로 한국은행 본관에서 열린 올해 마지막 금융통화위원회(금통위)에서는 1년 만에 기준금리를 인상하기로 결정했다.
금통위 이후 열린 기자간담회에서 이주열 총재는 이번 기준금리 상향 조정의 이유를 금융불균형 해소로 꼽았다. 금융불균형은 과도한 신용이 특정 부문으로 자금이 쏠리는 현상을 의미하는데, 한국은행은 가계부채의 누증을 중점적으로 들여다봤다. 이주열 총재는 "금융불균형을 보는 중요한 지표는 가계부채 누증 상황"이라고 말했다. 올해 3분기 가계신용은 1천514조원으로 전년 동기 대비 95조원(6.7%) 증가했다.
이 총재는 "금융불균형이 쌓인 이유는 저금리가 장기간 지속된 것 외에도 다른 요인이 복합적으로 작용했다"며 "정부가 거시건전성 정책 강화하고 있고 주택시장 안정대책을 펴고 있어서다. 소폭의 금리 조정이긴 하지만 금융안정 측면에서 불균형 축소에 효과가 있을 것"이라고 말했다.
이어 그는 통화정책만으로는 금융불균형을 전적으로 해소하기 어렵다는 조건을 달았다. 그는 "금융불균형 해소를 위해선 통화정책 등이 복합적으로 작용한다. 통화정책 말고도 다른 정책이 같이 가야 한다"고 설명했다.
'''
print( list( map( lambda a : (a, 1), msg.split(' ') ) ) )


# reduce
from functools import reduce
maplst = list( map( lambda a : (a, 1), msg.split(' ') ) )
reducelst = list( reduce( lambda a, b : (a + b), maplst ) )
for i in reducelst :
    print( i )








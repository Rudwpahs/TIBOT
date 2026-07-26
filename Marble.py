import random
from User import User

class Marble:
    def __init__(self, player, dobby):
        self.dobby = dobby
        self.player = player
        self.result = 0 # 매턴 마다 홀짝 결과 저장
        self.expec = 0 # 매턴 홀짝 예상 값

    def prtStatus(self):
        pNumber = self.player.getNumber()
        dNumber = self.dobby.getNumber()

        clear()
        print("%6s"% self.player.getName() + " : ", end="")
        for i in range(pNumber):
            print("🟡", end="")
        print()
        
        print("%6s"% self.dobby.getName() + " : ", end="")
        for i in range(dNumber):
            print("🟡", end="")
        print()

    def evaluate(self):
        if self.dobby.getNumber() == 0:
            clear()
            dobby_say("사용자님이 승리했어요! 🚀")
            return False
        elif self.player.getNumber() == 0:
            clear()
            dobby_say("티봇이 승리했어요! 🪄")
            return False
        else:
            return True
    
    def turn(self):
        dobby_say("홀짝을 예상해주세요!\n"+
                  "  1) 홀수\n"+
                  "  2) 짝수")
        self.expec = int(answer())    #예상값을 입력

    def oddeven(self):
        number_list = random.choice(range(1, self.dobby.getNumber()+1))
        if number_list % 2 == 0:
            dobby_say(f"{number_list}이므로 짝수입니다!")
            self.result = 2
        else:
            dobby_say(f"{number_list}이므로 홀수입니다!")
            self.result = 1

    def count(self):
        if self.result == self.expec:    #예상에 성공한 경우 티봇의봇 구슬이 감소
            self.dobby.dropNumber()
            dobby_say("사용자님이 맞추셨어요!!\n"+
                      "티봇의 구슬을 가져가셔도 좋아요....")

        elif self.result != self.expec:    #실패한 경우 플레이어의 구슬 감소
            self.player.dropNumber()
            dobby_say("아이쿠..사용자님 틀리셨네요\n"+
                      "사용자님의 구슬은 이제 제 것입니다!")

def game():
    player = User("User", 4)
    dobby = User("TiBot", 4)

    marble = Marble(player, dobby)

    marble.prtStatus()

    while(marble.evaluate()):
        marble.turn()
        marble.oddeven()
        marble.count()
        petc()
        marble.prtStatus()

if __name__ == "__main__":
    game()
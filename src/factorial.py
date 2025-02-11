def factorial(n: int) -> int:
    """
    n!을 계산해주는 함수
    n이 음수일 경우 예외(ValueError)를 발생
    """
    #if n < 0:
    #    raise ValueError("음수에 대해서는 팩토리얼을 구할 수 없습니다.")
    if n == 0:
        return 1

    result = 1
    for i in range(1, n+1):
        result *= i
    return result


if __name__ == "__main__":
    # 실행 예시
    print(factorial(5))  # 120
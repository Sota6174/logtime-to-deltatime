import datetime


def get_day(y: int, m: int, d: int) -> tuple:
    """日時指定が省略された際に、今日の日付に値を更新する

    Args:
        y (int): yaer
        m (int): month
        d (int): day

    Returns:
        tuple: year, month, day
    """
    today_utc = datetime.datetime.utcnow().date()
    if y == 0:
        y = today_utc.year
    if m == 0:
        m = today_utc.month
    if d == 0:
        d = today_utc.day
    return y, m, d


def set_time(h: int, m: int, s: int, *, year: int = 0, month: int = 0, day: int = 0) -> datetime.datetime:
    """日時を設定する
    hour, month, dayの指定が省略された場合は実行日の日付(UTF)に更新される

    Args:
        h (int): hour
        m (int): minute
        s (int): second
        year (int, optional): Defaults to 0.
        month (int, optional): Defaults to 0.
        day (int, optional): Defaults to 0.

    Returns:
        datetime.datetime

    Examples: 実行日が2022年1月23日の場合
        set_time(14, 4, 3) -> 2022-01-23 14:01:03
        set_time(14, 4, 3, day=21) -> 2022-01-21 14:01:03
        set_time(14, 4, 3, month=2, day=1) -> 2022-02-1 14:01:03
    """
    year, month, day = get_day(year, month, day)
    return datetime.datetime(year, month, day, h, m, s)


def format_deltatime(time: datetime.timedelta) -> str:
    """datetime.timedelta型の経過時間を日本語表記に変換する

    Args:
        time (datetime.timedelta): 経過時間

    Returns:
        str: 経過時間の日本語表記

    Examples: 実行日が2022年1月23日の場合
        format_deltatime(1 day, 6:00:35) -> 1日と 6時間0分35秒
    """
    m, s = divmod(time.seconds, 60)
    h, m = divmod(m, 60)
    t = f"{h}時間{m}分{s}秒"

    if time.days == 0:
        return t
    return f"{time.days}日と " + t


def calc(epoch: list, start, end):
    epoch_num = epoch[1] - epoch[0] + 1
    if type(start) == str:
        start = datetime.datetime.fromisoformat(start.split(',')[0])
        end = datetime.datetime.fromisoformat(end.split(',')[0])
    delta_time = abs(end - start)

    print(f"経過時間（epoch{epoch[0]}～{epoch[1]}）")
    print(delta_time)
    print(format_deltatime(delta_time))
    print()

    mean = delta_time / epoch_num
    print(f"1epochあたりの平均：\n{mean.seconds / 60:.2f}\n{format_deltatime(mean)}")


if __name__ == "__main__":
    epoch = [1, 11]
    start = set_time(14, 4, 38)
    end = set_time(20, 54, 38)
    calc(epoch, start, end)

    epoch = [1, 11]
    start = "2022-01-22 14:04:38,667"
    end = "2022-01-22 20:54:38,865"
    calc(epoch, start, end)

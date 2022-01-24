# logtime-to-deltatime

## 学習のログからトータルの実行時間及び、1epochあたりの実行時間を算出する

- [espnet](https://github.com/espnet/espnet)でTTSの学習の過程はtrain.logに出力されていく。このtrain.logから学習にかかる合計時間と1epochあたりの時間をログのコピペで出せるようにしたかった。
- 暗算で大雑把に計算するんでもいいし、学習とともに生成されるimagesフォルダ内にtrain_time.pngがあった

- 例
- 1epoch目が`2022-01-22 14:04:38,667`に始まり、30epoch目が`2022-01-22 20:54:38,865`に終わった場合
    - 入力例1
      - epoch = [1, 30]
      - start = "2022-01-22 14:04:38,667"
      - end = "2022-01-22 20:54:38,865"
    - 入力例2
      - epoch = [1, 30]
      - start = set_time(14, 4, 38, year=2022, month=1, day=22)
      - end = set_time(20, 54, 38, year=2022, month=1, day=22)
    - 入力例3(startとendが日付をまたがない場合)
      - year, month, dayは実行日が指定される
      - epoch = [1, 30]
      - start = set_time(14, 4, 38)
      - end = set_time(20, 54, 38)
    - 出力
      ```
      2022-01-24 14:04:38
      経過時間（epoch1～11）
      6:50:00
      6時間50分0秒

      1epochあたりの平均：
      37.27
      0時間37分16秒
      ```

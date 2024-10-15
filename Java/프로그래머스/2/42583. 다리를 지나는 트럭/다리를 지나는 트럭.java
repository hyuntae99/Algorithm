import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        int currentWeight = 0; // 다리 위에 있는 트럭들의 총 무게
        Queue<Integer> bridge = new LinkedList<>(); // 다리 위의 트럭들을 관리할 큐

        // 다리를 길이만큼 0으로 초기화 (아직 트럭이 없음)
        for (int i = 0; i < bridge_length; i++) {
            bridge.offer(0);
        }

        int index = 0; // 대기 중인 트럭 배열의 인덱스

        while (!bridge.isEmpty()) {
            answer++; // 매 초가 지남

            // 다리에서 트럭이 빠져나감 (맨 앞에 있는 트럭이 이동 완료됨)
            currentWeight -= bridge.poll();

            // 아직 대기 중인 트럭이 남아있는 경우
            if (index < truck_weights.length) {
                // 새로운 트럭이 다리에 올라갈 수 있는지 확인
                if (currentWeight + truck_weights[index] <= weight) {
                    // 트럭이 올라갈 수 있으면 다리에 진입
                    bridge.offer(truck_weights[index]);
                    currentWeight += truck_weights[index];
                    index++; // 다음 트럭으로 넘어감
                } else {
                    // 올라갈 수 없으면 0을 넣어서 시간을 벌음
                    bridge.offer(0);
                }
            }
        }

        return answer;
    }
}

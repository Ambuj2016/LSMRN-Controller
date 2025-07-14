// lnt_embedded.cpp

class LNTController {
public:
    float kp, ki, integral;

    LNTController() {
        kp = 0.5f;
        ki = 0.1f;
        integral = 0.0f;
    }

    float computeControl(float error) {
        integral += error;
        return kp * error + ki * integral;
    }
};

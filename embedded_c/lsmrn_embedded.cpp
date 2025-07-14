// lsmrn_embedded.cpp

#include "platform_config.h"
#include <cmath>

class LSMRNController {
public:
    float w1[HIDDEN_SIZE][INPUT_SIZE];
    float w2[HIDDEN_SIZE];
    float xc[INPUT_SIZE];

    LSMRNController() {
        for (int i = 0; i < HIDDEN_SIZE; ++i) {
            for (int j = 0; j < INPUT_SIZE; ++j)
                w1[i][j] = 0.05f * ((float)rand() / RAND_MAX - 0.5f);
            w2[i] = 0.05f * ((float)rand() / RAND_MAX - 0.5f);
        }
        for (int i = 0; i < INPUT_SIZE; ++i) xc[i] = 0.0f;
    }

    float forward(float input[INPUT_SIZE]) {
        float sum = 0.0f;
        for (int j = 0; j < HIDDEN_SIZE; ++j) {
            float Sj = 0.0f;
            for (int i = 0; i < INPUT_SIZE; ++i)
                Sj += w1[j][i] * input[i];
            float phi = tanh_approx(Sj);
            sum += w2[j] * phi;
        }
        return sum;
    }

    void updateWeights(float e_prev, float u_prev, float input[INPUT_SIZE]) {
        float delta = sqrtf(BETA_C * (e_prev + u_prev));

        for (int j = 0; j < HIDDEN_SIZE; ++j) {
            float Sj = 0.0f;
            for (int i = 0; i < INPUT_SIZE; ++i)
                Sj += w1[j][i] * input[i];

            // Update w2
            w2[j] = delta / (Sj + LAMBDA_1);

            // Update w1
            for (int i = 0; i < INPUT_SIZE; ++i) {
                float denom = input[i] + LAMBDA_2;
                float numer = sat(delta / (w2[j] + LAMBDA_3));
                w1[j][i] = numer / denom;
            }
        }
    }
};

#include "lsmrn_embedded.cpp"  // or lnt_embedded.cpp

LSMRNController ctrl;
float input[INPUT_SIZE] = {0.1, 0.2, 0.3, 0.4};

void loop() {
    float control = ctrl.forward(input);
    float error = 0.5f; // placeholder
    float u_prev = control;  // feedback or estimate
    ctrl.updateWeights(error, u_prev, input);
}

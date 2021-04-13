#ifndef DENM_BASIC_SERVICE_THREAD_H
#define DENM_BASIC_SERVICE_THREAD_H

#include "cruntime.h"
#include "c_thread.h"

struct denm_basic_service_thread{
    struct thread base_thread;
    int global_init_done;
};


void* denmbasicservicethread_get_this_pointer(struct denm_basic_service_thread *self);
status_t denmbasicservicethread_init_basic(struct denm_basic_service_thread *self);
status_t denmbasicservicethread_init(struct denm_basic_service_thread *self);
status_t denmbasicservicethread_destroy(struct denm_basic_service_thread *self);
status_t denmbasicservicethread_run(struct denm_basic_service_thread *self);
status_t denm_basic_service_init();
status_t denm_basic_service_destroy();


#endif // !DENM_BASIC_SERVICE_THREAD_H

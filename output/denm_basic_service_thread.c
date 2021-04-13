#include "denm_basic_service_thread.h"

#include "xlog.h"
#include "mem_tool.h"
#include "globals.h"

THREAD_VIRTUAL_FUNCTIONS_DEFINE(struct denm_basic_service_thread, denmbasicservicethread)
/******************************************************/
void* denmbasicservicethread_get_this_pointer(struct denm_basic_service_thread *self)
{
    return (void*)self;
}

status_t denmbasicservicethread_init_basic(struct denm_basic_service_thread *self)
{
    thread_init_basic(&self->base_thread);
    self->global_init_done = 0;
    return STATUS_OK;
}

status_t denmbasicservicethread_init(struct denm_basic_service_thread *self)
{
    denmbasicservicethread_init_basic(self);
    thread_init(&self->base_thread);
    THREAD_INIT_VIRTUAL_FUNCTIONS(denmbasicservicethread);
    return STATUS_OK;
}

status_t denmbasicservicethread_destroy(struct denm_basic_service_thread *self)
{
    thread_base_destroy(&self->base_thread);
    denmbasicservicethread_init_basic(self);
    return STATUS_OK;
}

status_tdenmbasicservicethread_run(struct denm_basic_service_thread *self)
{
    globals_init(&g_globals);
    self->global_init_done = 1;
    globals_main_loop(&g_globals);
    globals_destroy(&g_globals);
    return STATUS_OK;
}

/*****************************************************/
static struct denm_basic_service_thread g_denmbasicservicethread;

status_t denm_basic_service_init()
{
    static int has_init = 0;
    if( has_init == 0)
    {
        has_init = 1;
        denmbasicservicethread_init(&g_denmbasicservicethread);
        thread_start(&g_denmbasicservicethread.base_thread);
        while(!g_denmbasicservicethread.global_init_done)
        {
            LOGE("wait init");
            usleep(10 * 1000);
        }
    }
    return STATUS_OK;
}

status_t denm_basic_service_destroy()
{
    globals_quit_main_loop(&g_globals);
    thread_stop(&g_denmbasicservicethread.base_thread);
    thread_wait_complete(&g_denmbasicservicethread.base_thread,5000);
    denmbasicservicethread_destroy(&g_denmbasicservicethread);
    return STATUS_OK;
}



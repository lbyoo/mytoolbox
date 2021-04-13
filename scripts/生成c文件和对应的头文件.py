#coding:utf-8
import os
type = "0"                          # 0 空文件， 1 thread
model_name = "palloc"
prefix = "gps_watcher"



def main():
    head_file = os.path.join("../output", "%s.h" % prefix)
    body_file = os.path.join("../output", "%s.c" % prefix)

    #generate c header file
    with open(head_file, "w") as f:
        f.write("#ifndef _%s_H_INCLUDED_\n" % prefix.upper())
        f.write("#define _%s_H_INCLUDED_\n" % prefix.upper())
        if type == "1":
            f.write(template[type][0].format(prefix, prefix.replace("_", ""), model_name) )

        f.write("#include \"lby_config.h\"\n")
        f.write("#include \"lby_core.h\"")
        f.write("\n\n");
        f.write("#endif //_%s_H_INCLUDED_\n" % prefix.upper())

    #generate c body file
    with open(body_file, "w") as f:
        f.write("#include \"lby_config.h\"\n")
        f.write("#include \"lby_core.h\"")
        if type == "1":
            f.write(template[type][1].format(prefix, prefix.replace("_", ""), model_name))
        f.write("\n\n");


# template is here
template = {
    "0":"",
    "1": [r"""
#include "cruntime.h"
#include "c_thread.h"

struct {0}{{
    struct thread base_thread;
    int global_init_done;
}};


void* {1}_get_this_pointer(struct {0} *self);
status_t {1}_init_basic(struct {0} *self);
status_t {1}_init(struct {0} *self);
status_t {1}_destroy(struct {0} *self);
status_t {1}_run(struct {0} *self);
status_t {2}_init();
status_t {2}_destroy();
""", r"""
#include "xlog.h"
#include "mem_tool.h"
#include "globals.h"

THREAD_VIRTUAL_FUNCTIONS_DEFINE(struct {0}, {1})
/******************************************************/
void* {1}_get_this_pointer(struct {0} *self)
{{
    return (void*)self;
}}

status_t {1}_init_basic(struct {0} *self)
{{
    thread_init_basic(&self->base_thread);
    self->global_init_done = 0;
    return STATUS_OK;
}}

status_t {1}_init(struct {0} *self)
{{
    {1}_init_basic(self);
    thread_init(&self->base_thread);
    THREAD_INIT_VIRTUAL_FUNCTIONS({1});
    return STATUS_OK;
}}

status_t {1}_destroy(struct {0} *self)
{{
    thread_base_destroy(&self->base_thread);
    {1}_init_basic(self);
    return STATUS_OK;
}}

status_t {1}_run(struct {0} *self)
{{
    self->global_init_done = 1;
    while(self.)
    {
        printf("this is in the thread\n");
        crt_msleep(1000);
    }
    return STATUS_OK;
}}

/*****************************************************/
static struct {0} g_{1};

status_t {2}_init()
{{
    static int has_init = 0;
    if( has_init == 0)
    {{
        has_init = 1;
        {1}_init(&g_{1});
        thread_start(&g_{1}.base_thread);
        while(!g_{1}.global_init_done)
        {{
            LOGE("wait init");
            crt_msleep(10);
        }}
    }}
    return STATUS_OK;
}}

status_t {2}_destroy()
{{
    thread_stop(&g_{1}.base_thread);
    thread_wait_complete(&g_{1}.base_thread,5000);
    {1}_destroy(&g_{1});
    return STATUS_OK;
}}
"""],
}

if __name__ == '__main__':
    main()



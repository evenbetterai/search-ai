from threading import Thread


class ThreadWithReturn(Thread):
    
    @staticmethod
    def create_and_start_threads(n, target_func, args_tup):
        threads_list = []
        
        for i in range(n):
            t = ThreadWithReturn(target=target_func, args=args_tup[i])
            threads_list.append(t)
            t.start()
        
        return threads_list
    
    def __init__(
            self,
            group=None,
            target=None,
            name=None,
            args=(),
            kwargs={}
    ):
        super(ThreadWithReturn,
              self).__init__(group,
                             target,
                             name,
                             args,
                             kwargs)
        
        self._return = None
    
    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)
    
    def join(self, *args):
        super(ThreadWithReturn, self).join(*args)
        return self._return

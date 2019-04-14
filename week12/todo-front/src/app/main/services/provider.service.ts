import { Injectable } from '@angular/core';
import {ExService} from './ex.service';
import {HttpClient} from '@angular/common/http';
import {Task,TaskList} from '../models/model'
@Injectable({
  providedIn: 'root'
})
export class ProviderService extends ExService {

  constructor(http:HttpClient) {
    super(http);
   }
   getTaskLists(): Promise<TaskList[]>{
     return this.get(`http://127.0.0.1:8000/api/task_lists/`,{});
   }
   getExactList(id: number): Promise<TaskList>{
     return this.get(`http://127.0.0.1:8000/api/task_lists/${id}/`,{id});
   }
   getTasks(id: number): Promise<Task[]> {
    return this.get(`http://127.0.0.1:8000/api/task_lists/${id}/tasks/`, {id});
  }
  createTaskList(name:any):Promise<TaskList>{
    return this.post(`http://127.0.0.1:8000/api/task_lists/`, {
      name: name
    });
  }
  updateTaskList(list:TaskList):Promise<TaskList>{
    return this.put(`http://127.0.0.1:8000/api/task_lists/${list.id}/`, {
      name: list.name
    });
  }
  deleteTaskList(id:Number):Promise<any>{
    return this.delet(`http://127.0.0.1:8000/api/task_lists/${id}/`,{})
  }
}

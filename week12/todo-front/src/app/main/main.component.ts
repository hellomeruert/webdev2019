import { Component, OnInit, OnDestroy } from '@angular/core';
import {ProviderService} from './services/provider.service';
import {Task,TaskList} from './models/model';
import { loadInternal } from '@angular/core/src/render3/util';
import { checkAndUpdateBinding } from '@angular/core/src/view/util';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {
  public taskLists:TaskList[]=[];
  public curList:TaskList;
  public tasks: Task[]=[];
  public update='';
  public name='';
  public task_name='';
  constructor(private provider: ProviderService) { }

  ngOnInit() {
    this.provider.getTaskLists().then(res=>{
      this.taskLists=res;
    });
  }
  
  getExList(list: TaskList) {
    this.provider.getExactList(list.id).then(res => {
      this.curList=res;
      console.log(this.curList);
    });
  }
  getTasks(l:TaskList){
    this.curList=l;
   
    this.provider.getTasks(l.id).then(res=>{
      this.tasks=res;
    });
  }
  createTaskList(){
    if(this.name!==''){
      this.provider.createTaskList(this.name).then(res=>{
        this.name='';
        this.taskLists.push(res);
      });
    }
  }
  deleteTaskList(li:TaskList){
    this.provider.deleteTaskList(li.id).then(res=>{
      console.log(li.name+"deleted");
      this.provider.getTaskLists().then(r=>{
        this.taskLists=r;
      });
    });
  }
  updateTaskList(c: TaskList) {
    this.hide(c);
    if(this.update!=''){
      c.name=this.update;
      this.update='';
      this.provider.updateTaskList(c).then(res => {
      console.log(c.name);
    });
  }
  }
  hide(h:TaskList){
    var k=document.getElementById(h.id+"");
    var pr=document.getElementById(h.name).getElementsByTagName("img")[1];
   if(k.style.getPropertyValue("visibility")!="visible"){
               k.style.setProperty("visibility","visible");
    }else{
      k.style.setProperty("visibility","hidden");
    }
    console.log(k);
  }
}

  



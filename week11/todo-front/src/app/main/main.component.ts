import { Component, OnInit, OnDestroy } from '@angular/core';
import {ProviderService} from './services/provider.service';
import {Task,TaskList} from './models/model';
import { loadInternal } from '@angular/core/src/render3/util';


@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  public taskLists:TaskList[]=[];
  public curList:TaskList;
  public tasks: Task[]=[];
  public loading=true;
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
    this.provider.getTasks(l.id).then(res=>{
      this.tasks=res;
      if (res.length>0){
        this.loading=true;
      }else{
        this.loading=false;
      }

    });
  }
}
